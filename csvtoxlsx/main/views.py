from django.shortcuts import render, redirect
from django.http import JsonResponse , FileResponse
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.conf import settings  # Import settings for MEDIA_ROOT
from .models import UserModel , DocumentsModel
import pandas as pd
from django.utils.timezone import now
import os
@csrf_exempt
def register(request):
    """Handles user registration with UserModel."""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            return JsonResponse({"error": "Username and password are required"}, status=400)

        try:
            user = UserModel.objects.create_user(username=username, password=password)  # Using custom manager
            return JsonResponse({"message": "User registered successfully", "user_id": user.id})
        except IntegrityError:
            return JsonResponse({"error": "Username already exists"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt


def login(request):
    """Handles user login without using Django's built-in authentication."""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            return JsonResponse({"error": "Username and password are required"}, status=400)

        try:
            user = UserModel.objects.get(username=username)
            if user.password == password:  # plain-text password check
                request.session['user_id'] = str(user.id)  # Storing user ID in session
                request.session['username'] = user.username
                return JsonResponse({"message": "Login successful"})
            else:
                return JsonResponse({"error": "Invalid credentials"}, status=401)
        
        except UserModel.DoesNotExist:
            return JsonResponse({"error": "User does not exist"}, status=404)

    return JsonResponse({"error": "Invalid request method"}, status=405)

@csrf_exempt

def upload(request):
    if request.method == "POST":
        if not request.session.get('user_id'):
            return JsonResponse({"error": "Not Authenticated."}, status=403)

        user_id = request.session.get('user_id')
        user = UserModel.objects.get(id=user_id)  
        file = request.FILES.get("file")
        if not file:
            return JsonResponse({"error": "No file provided."}, status=400)
        if not file.name.endswith(".csv"):
            return JsonResponse({"error": "Only CSV files are allowed."}, status=400)

        try:
            # Save document information in the database
            document = DocumentsModel.objects.create(
                document_name=file.name,
                created_at=now(),
                userid=user  # Assigning the actual UserModel instance to the foreign key field
            )

            # Convert CSV to XLSX
            df = pd.read_csv(file)

            # Define a persistent storage directory
            output_dir = os.path.join(settings.MEDIA_ROOT, "converted_files")
            os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

            # Save the file as XLSX
            output_file_path = os.path.join(output_dir, f"{document.document_name.replace('.csv', '.xlsx')}")
            df.to_excel(output_file_path, index=False)

            # Return the converted XLSX file
            return FileResponse(
                open(output_file_path, "rb"),
                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                as_attachment=True,
                filename=document.document_name.replace('.csv', '.xlsx')
            )

        except Exception as e:
            print(e)
            return JsonResponse({"error": f"File processing error: {e}"}, status=500)

    return JsonResponse({"error": "Invalid request method. Use POST."}, status=400)
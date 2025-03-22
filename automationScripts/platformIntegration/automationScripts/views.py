from django.shortcuts import render

from django.http import JsonResponse
from django.views import View
from django.urls import path
import subprocess
import json
import logging

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Configure logging
logger = logging.getLogger(__name__)

@method_decorator(csrf_exempt, name='dispatch')  # Disable CSRF for this view
class UpdateGitHubView(View):
    """
    Handles POST requests to trigger a GitHub update script.
    """
    def post(self, request, *args, **kwargs):
        try:
            result = subprocess.run(["python", "automationScripts/update_github.py"], capture_output=True, text=True, check=True)
            return JsonResponse({"message": "GitHub update triggered", "output": result.stdout}, status=200)
        except subprocess.CalledProcessError as e:
            logger.error(f"GitHub update error: {e.stderr}")
            return JsonResponse({"error": "GitHub update failed", "details": e.stderr}, status=500)
        except Exception as e:
            logger.exception("Unexpected error during GitHub update")
            return JsonResponse({"error": "Internal server error"}, status=500)

@method_decorator(csrf_exempt, name='dispatch')  #  Disable CSRF for this view
class ProcessDataView(View):
    """
    Handles POST requests to process JSON data and return modified data.
    """
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))
            
            if not isinstance(data, dict):
                return JsonResponse({"error": "Invalid JSON format. Expected a dictionary."}, status=400)
            
            processed_data = {k: v.upper() if isinstance(v, str) else v for k, v in data.items()}
            
            return JsonResponse({"processed_data": processed_data}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON payload"}, status=400)
        except Exception as e:
            logger.exception("Unexpected error during data processing")
            return JsonResponse({"error": "Internal server error"}, status=500)


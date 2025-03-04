from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Panggil default exception handler
    response = exception_handler(exc, context)

    if response is not None:
        # Tambahkan atau ubah format JSON di sini
        response.data['status_code'] = response.status_code
        # response.data['message'] = 'Custom message for errors'
    
    return response
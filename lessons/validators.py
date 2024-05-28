from rest_framework.serializers import ValidationError


class YTValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, link):
        youtube = 'https://youtube.com/'

        if link.get('video_link'):
            if youtube not in link.get('video_link'):
                raise ValidationError('Необходимо вставить ссылку на youtube')
        else:
            return None

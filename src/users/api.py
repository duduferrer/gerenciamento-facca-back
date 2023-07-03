from typing import List
from .schemas import UserSchemaOnList, UserInputSchema, UserOutputSchema
from facca.api import api
from .models import User
from django.shortcuts import get_object_or_404

# TODO implementar verificacao usuario


@api.get('users/', response=List[UserSchemaOnList])
def get_user_list(request):
    res = User.objects.all()
    return res


@api.post('users/')
def create_user(request, payload: UserInputSchema):
    user_dict = payload.dict()
    user = User.objects.create(
        **payload.dict(), is_active=True, role='U', balance=0)
    password = user_dict['password']
    user.set_password(password)
    user.save()
    return user.id


@api.delete('users/{user_id}')
def delete_user(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return {"success": True}


@api.get('users/{user_id}', response=UserOutputSchema)
def get_user(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    return user

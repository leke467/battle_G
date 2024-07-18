from rest_framework import generics, status
from rest_framework.response import Response


# create squad
class SquadCreateBase(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        squad_id = request.data.get(self.squad_id_field)
        if self.queryset.filter(**{self.squad_id_field: squad_id}).exists():
            return Response({"error": "Squad already exists"}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)





# update squad details
class SquadRetrieveUpdateDestroyBase(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        squad = self.get_object().get(pk=pk)
        squad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





#view squads



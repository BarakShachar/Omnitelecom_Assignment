from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from callretriver.api.serializers import CompanySerializer, TeamSerializer, UserSerializer
from callretriver.models import Company, Team, User, Call
from rest_framework import status


class CompanyView(APIView):

    def post(self, request: Request) -> Response:
        company_serializer: CompanySerializer = CompanySerializer(data=request.data)
        if not company_serializer.is_valid():
            response: Response = Response({"details": company_serializer.errors},
                                          status=status.HTTP_400_BAD_REQUEST)
        else:
            company: Company = company_serializer.save()
            response: Response = Response({"company id": company.id},
                                          status=status.HTTP_201_CREATED)
        return response


class TeamView(APIView):

    def post(self, request: Request) -> Response:
        data: dict = dict(request.data)
        if data.get("company_parent") is None and data.get("team_parent") is None:
            response: Response = Response({"details": "provide team parent or company parent"},
                                          status=status.HTTP_400_BAD_REQUEST)
        elif data.get("company_parent") is not None and data.get("team_parent") is not None:
            response: Response = Response({"details": "provide just 1 parent"},
                                          status=status.HTTP_400_BAD_REQUEST)
        else:
            team_serializer: TeamSerializer = TeamSerializer(data=request.data)
            if not team_serializer.is_valid():
                response: Response = Response({"details": team_serializer.errors},
                                              status=status.HTTP_400_BAD_REQUEST)
            else:
                team: Team = team_serializer.save()
                response: Response = Response({"team id": team.id},
                                              status=status.HTTP_201_CREATED)
        return response


class UserView(APIView):

    def post(self, request: Request) -> Response:
        data: dict = dict(request.data)
        if data.get("company_parent") is None and data.get("team_parent") is None:
            response: Response = Response({"details": "provide team parent or company parent"},
                                          status=status.HTTP_400_BAD_REQUEST)
        elif data.get("company_parent") is not None and data.get("team_parent") is not None:
            response: Response = Response({"details": "provide just 1 parent"},
                                          status=status.HTTP_400_BAD_REQUEST)
        else:
            user_serializer: UserSerializer = UserSerializer(data=request.data)
            if not user_serializer.is_valid():
                response: Response = Response({"details": user_serializer.errors},
                                              status=status.HTTP_400_BAD_REQUEST)
            else:
                user: User = user_serializer.save()
                response: Response = Response({"user id": user.id},
                                              status=status.HTTP_201_CREATED)
        return response


class CallView(APIView):

    def get(self, request: Request, call_id: int) -> Response:
        try:
            user_request: User = User.objects.get(id=request.query_params.get("user"))
            call: Call = Call.objects.get(id=call_id)
            call_owner: User = call.owner
            if call_owner.company_parent is not None:
                parent = call_owner.company_parent
            else:
                parent = call_owner.team_parent
            while parent is not None:
                if parent == user_request.company_parent:
                    return Response({"call data": call.data}, status=status.HTTP_201_CREATED)
                if parent == user_request.team_parent:
                    return Response({"call data": call.data}, status=status.HTTP_201_CREATED)
                if parent.company_parent is not None:
                    parent = parent.company_parent
                elif type(parent) != Company and parent.team_parent is not None:
                    parent = parent.team_parent
                else:
                    parent = None
            response: Response = Response({"details": "error"}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            response: Response = Response({"details": "error"}, status=status.HTTP_400_BAD_REQUEST)
        return response


class AllowedUsers(APIView):
    def get(self, request: Request, user_id: int) -> Response:
        user_owner: User = User.objects.get(id=user_id)


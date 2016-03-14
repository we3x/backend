from flask_restplus import fields
from . import api


# Roles fields

roles_fields = api.model(
    'Roles', {
        'name': fields.String(required=True),
        'description': fields.String(required=True),
        'admin': fields.String(required=True),
    }
)


# User fields
user_base = api.model(
    'User', {
        'email': fields.String(
            description='The email',
            required=True,
            default='admin@example.com'
        ),
        'first_name': fields.String,
        'last_name': fields.String,
    }
)


user_body = api.clone(
    'User password', user_base, {
        'password': fields.String(
            description='Password',
            required=True,
            default='Sekrit',
        )
    }
)

user_response = api.clone(
    'Get User', user_base, {
        'id': fields.String,
        'roles': fields.Nested(roles_fields),
    }
)


# Auth fields
auth_fields = api.model(
    'Auth', {
        'email': fields.String(
            description='The email',
            required=True,
            default='admin@example.com'
        ),
        'password': fields.String(
            description='The password',
            required=True,
            default='Sekrit'
        ),
    }
)

token_response = api.model(
    'Token', {
        'token': fields.String,
    }
)

# Application fields
application_fields = api.model(
    'Application', {
        'galaxy_role': fields.String(required=True),
        'name': fields.String(required=True),
    }
)

# Provider fields
provider_fields = api.model(
    'Provider', {
        'name': fields.String(required=True),
        'type': fields.String(required=True),
    }
)


# Cluster fields
cluster_fields = api.model(
    'Cluster', {
        'name': fields.String(required=True),
    }
)

get_cluster_fields = api.clone('Get Clusters', cluster_fields, {
    'providers': fields.Nested(provider_fields),
    'id': fields.String,
    'roles': fields.Nested(roles_fields),
    'services': fields.String,
}
)

# Task fields
task_fields = api.model(
    'Task', {
        'id': fields.String,
        'celery_id': fields.String,
    }
)


# Host fields
host_fields = api.model(
    'Host', {
        'hostname': fields.String,
        'ip': fields.String,
    }
)

# Service fields
service_fields = api.model(
    'Service', {
        'name': fields.String(required=True),
    }
)

post_service_fields = api.model(
    'Post Service',
    {'service': fields.String},
)

get_service_fields = api.clone('Get Services', service_fields, {
    'id': fields.String,
    'name': fields.String,
    'applications': fields.Nested(application_fields),
    'user': fields.Nested(user_response),
})

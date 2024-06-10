class CategoryItem:
    def __init__(self, expression, variables):
        self.expression = expression
        self.variables = variables


class CategoryArtifacts:
    def __init__(self, image, function, pas_droplet):
        self.image = image
        self.function = function
        self.pas_droplet = pas_droplet


class CategoryWorkloads:
    def __init__(self, os, kubernetes, cf):
        self.os = os
        self.kubernetes = kubernetes
        self.cf = cf


class CategoryInfrastructure:
    def __init__(self, kubernetes, os):
        self.kubernetes = kubernetes
        self.os = os


class Categories:
    def __init__(self, artifacts, workloads, infrastructure, entity_scope):
        self.artifacts = artifacts
        self.workloads = workloads
        self.infrastructure = infrastructure
        self.entity_scope = entity_scope


class ApplicationScope:
    def __init__(self, name, categories, description, author, updated):
        self.name = name
        self.categories = categories
        self.description = description
        self.author = author
        self.updated = updated


# Sample to create the objects
# image_item = CategoryItem("v1", [{"attribute": "aqua.registry", "value": "Docker Hub", "name": ""}])
# function_item = CategoryItem("v1", [{"attribute": "aqua.registry", "value": "Docker Hub", "name": ""}])
# pas_droplet_item = CategoryItem("v1", [{"attribute": "aqua.registry", "value": "Docker Hub", "name": ""}])
# artifacts = CategoryArtifacts(image_item, function_item, pas_droplet_item)

# os_workload_item = CategoryItem("v1", [{"attribute": "aqua.registry", "value": "Docker Hub", "name": ""}])
# kubernetes_workload_item = CategoryItem("v1", [{"attribute": "aqua.registry", "value": "Docker Hub", "name": ""}])
# cf_workload_item = CategoryItem("v1", [{"attribute": "aqua.registry", "value": "Docker Hub", "name": ""}])
# workloads = CategoryWorkloads(os_workload_item, kubernetes_workload_item, cf_workload_item)

# kubernetes_infra_item = CategoryItem("v1", [{"attribute": "aqua.registry", "value": "Docker Hub", "name": ""}])
# os_infra_item = CategoryItem("v1", [{"attribute": "aqua.registry", "value": "Docker Hub", "name": ""}])
# infrastructure = CategoryInfrastructure(kubernetes_infra_item, os_infra_item)

# entity_scope_item = CategoryItem("v1", [{"attribute": "aqua.registry", "value": "Docker Hub", "name": ""}])

# categories = Categories(artifacts, workloads, infrastructure, entity_scope_item)

# ApplicationScope = ApplicationScope(
#     "My Application Scope",
#     categories,
#     "This is a description",
#     "John Doe",
#     "2023-04-18"
# )

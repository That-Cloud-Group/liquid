class Role:
    def __init__(
        self, name, description, author, updated, ui_access, is_super, actions
    ):
        self.name = name
        self.description = description
        self.author = author
        self.updated = updated
        self.ui_access = ui_access
        self.is_super = is_super
        self.actions = actions

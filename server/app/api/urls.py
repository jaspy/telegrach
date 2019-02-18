from .routes import *

api.add_url_rule('/api/posts', view_func=return_posts, methods=['GET']) 
api.add_url_rule('/api/posts', view_func=create_post, methods=['POST'])
api.add_url_rule('/api/posts/<slug>', view_func=return_post_by_slug, methods=['GET'])
api.add_url_rule('/api/posts/<slug>', view_func=delete_post, methods=['DELETE'])
api.add_url_rule('/api/posts/<slug>', view_func=update_post, methods=['PUT'])

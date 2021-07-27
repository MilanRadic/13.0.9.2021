from magiclink.helpers import create_magiclink

# Returns newly created from magiclink.models.MagicLink instance
magiclink = create_magiclink(email, request, redirect_url='')

# Generates the magic link url and sends it in an email
magiclink.send(request)

# If you want to build the magic link from the model instance but don't want to
#  send the email you can you can use:
magic_link_url = magiclink.generate_url(request)
import Image, ImageFont, ImageDraw
import base64
from os import path
from django.conf import settings
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.utils.encoding import smart_str

class img_replacement:
	data = None
	image_path = path.join(settings.MEDIA_ROOT, 'image_replacement', 'images')
	font_path = path.join(settings.MEDIA_ROOT, 'image_replacement', 'fonts')
	
	def __init__(self, data):
		self.data = data
		self.data['id'] = base64.b64encode(smart_str(''.join(self.data.values())))
		self.data['size'] = int(self.data['size'])
		
		# Check if file exists
		if not path.isfile(path.join(self.image_path, self.data['id'] + ".png")):
			
			## Open & copy image
			# We could use:
			# image = Image.new('RGBA', (len(data['text'])*data['size'], data['size']), (0,0,0,0))
			# But for some reason that creates a small drop shadow artifact under the text.
			
			clear = Image.open(path.join(self.image_path, "clear.png"))
			image = clear.copy()
			
			# Set font
			f = ImageFont.truetype(path.join(self.font_path, data['font']), data['size'])
			
			# Set img size
			image = image.resize(f.getsize(self.data['text']))

			# Draw
			draw = ImageDraw.Draw(image)
			draw.text((0, 0), data['text'], font=f, fill=self.data['color'])
			
			# Save
			image.save(path.join(self.image_path, data['id'] + ".png"), 'PNG')

	def __getitem__(self, key):
		return self.data[key]


register = template.Library()

@register.filter
@stringfilter
def image_replacement(value, info, autoescape=None):
	info = info.split(', ')
	args = {
		'text': value,
		'font': info[0],
		'size': info[1],
		'color': info[2],
		}
	image = img_replacement(args)
	args['image_path'] = "%simage_replacement/images/%s.png" % (settings.MEDIA_URL, image['id'])
	result = render_to_string("utils/image_replacement.html", args)
	return mark_safe(result)

@register.filter
@stringfilter
def image_replacement_path(value, info, autoescape=None):
	info = info.split(', ')
	args = {
		'text': value,
		'font': info[0],
		'size': info[1],
		'color': info[2],
		}
	image = img_replacement(args)
	return "%simage_replacement/images/%s.png" % (settings.MEDIA_URL, image['id'])

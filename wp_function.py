from base64 import b64encode
import os
from dotenv import load_dotenv
load_dotenv()


def wp_paragraph(text):
    code =f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return code

def wp_list(any_list):
    first_line = '<!-- wp:list --><ul><!-- wp:list-item -->'
    for lst in any_list:
        first_line += f'<li>{lst}</li>'
    end_line = '<!-- /wp:list-item --></ul><!-- /wp:list -->'
    code = f'{first_line}{end_line}'
    return code

def dictionary_list(dicts):
    
    first_line = '<!-- wp:list --><ul><!-- wp:list-item -->'
    for key, value in dicts.items():
        first_line += f'<li><strong>{key.title()}</strong> : {value.title()}</li>'
    end_line = '<!-- /wp:list-item --></ul><!-- /wp:list -->'
    code = f'{first_line}{end_line}'
    return code
def wp_image(src,name):
    code = f'<!-- wp:image {{"align":"center","id":747,"sizeSlug":"large","linkDestination":"none"}} --> <figure class="wp-block-image aligncenter size-large"><img src="{src}" alt="{name}" class="wp-image-747"/><figcaption class="wp-element-caption">{name}</figcaption></figure> <!-- /wp:image -->' 
    return code
def open_ai_data(prompt):
    import openai
    openai.api_key = os.getenv('openai_api')

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.4,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text = response.get('choices')[0].get('text').strip()
    return text
# def wp_content(*args):
#     i=0
#     code=''
#     for arg in args:
#         code += arg
#     i += 1
#     return code

wp_password = os.getenv('wp_pass')
def wp_headers(username):
    crediential = f'{username}:{wp_password}'
    token = b64encode(crediential.encode())
    code = {'authorization' : f'Basic {token.decode("utf-8")}'}
    return code

def wp_heading(text):
    """
   
    """
    return f' <!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'




    

from requests import get,post
from wp_function import wp_image,wp_list,wp_heading,wp_headers,wp_paragraph,dictionary_list,open_ai_data
meal_api = 'https://www.themealdb.com/api/json/v1/1/search.php?f=p'
res = get(meal_api)
jsn_data = res.json()
meals = jsn_data.get('meals')[0]
meal_name = meals.get('strMeal')
meal_area = meals.get('strArea')
meal_instruction = meals.get('strInstructions').split('\r\n')
meal_img = meals.get('strMealThumb')

i = 1
ingredient_dict = {}

while i<=20:
    key_ingredient = f'strIngredient{i}'
    value_measure = f'strMeasure{i}'
    if (meals.get(key_ingredient) != None) and (meals.get(key_ingredient) != ''):
        ingredient_dict[meals.get(key_ingredient)] = meals.get(value_measure)

    i += 1
# print(meal_instruction)




# organize all content 

title =open_ai_data(f'write seo-friendly title for {meal_area} {meal_name} receipe')
image = wp_image(meal_img,meal_name)
intro = open_ai_data(f'Write a seo-friendly intro about {title}')
heading_one = wp_heading('Ingredients list')
ingredient = dictionary_list(ingredient_dict)
heading_two = wp_heading(f'{meal_name} Descriptions')
descriptions = wp_list(meal_instruction)
slugs = meal_name.lower().strip().replace(' ','-')
conclusion = open_ai_data(f'write a short conclusion about {title}')

intro_html = wp_paragraph(intro)
concl_html = wp_paragraph(conclusion)

all_content = f'{image},{intro_html},{heading_one},{ingredient},{heading_two},{descriptions},{concl_html}'

# making data 

wp_data = {

    'title'     : title,
    'slug'      :slugs,
    'content'   : all_content

}

header = wp_headers('Mohammad')
wp_post_url ='https://dev-moprojects.pantheonsite.io/wp-json/wp/v2/posts'
post(wp_post_url, data=wp_data, headers=header)
print(f'{meal_area} {meal_name} is posted! Enjoy')
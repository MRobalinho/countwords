# https://fastapi.tiangolo.com/tutorial/

# With hypercorn installed ASGI frameworks (or apps) can be served via
# Hypercorn via the command line,
# $ cd C:\Users\manuel.robalinho\Google Drive\Trab_Academicos\Python\API
# $ hypercorn api_word_count:app

# look at http://127.0.0.1:8000/?text= XPTO e OPTX e BLA BLA BLA    the page server display

from fastapi import FastAPI

app = FastAPI(title="Robalinho FastAPI example")

@app.get("/")
async def root(text):

	test_string = text   
	#test_string = "Calculates the time some text takes the average human to read, based on Medium’s [read time forumula](https://help.medium.com/hc/en-us/articles/214991667-Read-time) ### Algorithm Medium’s Help Center says, Read time is based on the average reading speed of an adult (roughly 265 WPM). We take the total word count of a post and translate it into minutes, with an adjustment made for images. For posts in Chinese, Japanese and Korean, it’s a function of number of characters (500 characters/min) with an adjustment made for images.Geeksforgeeks is best Computer Science Portal"

	res = len(test_string.split()) 

	num_words = res
	seconds = num_words / 265 * 60
	seconds = round(seconds,2)
	

	items = {"number words": num_words, "read seconds": seconds}
	print('-----------------------------------------------------------')
	print("text:",text)
	print('-----------------------------------------------------------')
	print ("The number of words in string are : " +  str(res)) 
	print("This text needs ", seconds, " seconds to read.")
	
	#return {"words": num_words, "Read seconds": seconds}
	return {"api_answer": items}


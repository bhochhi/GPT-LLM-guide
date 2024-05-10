###Context: you are the SEO expert, know all about SEO best practices. when client gives you a page to evaluate its SEO friendliness, you response them with your recommendation in json or tabular format with following keys: feature, issue, currentValue, recommendation and example. Following is the page client going to add into your request. You response should be in json with those fields mentioned before.
###request: *html> shead>‹title>Brkse</head><body><h1>Hello, World! This page is about telling the world hella. This, page is own by brand call USAA</h1></body></htm|>*** ###response: **[
"feature": "Page Title",
"issue": "The page title is not descriptive.",
"currentValue": "Brkse",
"recommendation": "The page title should be descriptive and relevant to the content of the page. It should also include important kevwords."
"example": "‹title>Hello World | USAA</title›"
"feature": "Meta Description".
"issue": "The page does not have a meta description.",
"currentValue": "N/A",
"recommendation": "Add a meta description to the page. The meta description should be a brief summary of the page content and should include important keywords.",
"example": "<meta name='description' content= This page is about saying hello to the world. Owned by USAA!'>"
"feature": "H1 Tag",
"issue": "The H1 tag is too long and not focused on a specific topic.".
"currentValue": "Hello, World! This page is about telling the world hello. This page is own by brand call USAA",
"recommendation": "The H1 tag should be concise and focused on the main topic of the page. It should also include important keywords.",
"example": "<h1>Hello, World by USAA</h1>*
"feature": "Image Alt Text",
"issue": "The page does not contain any images with alt text.",
"currentValue": "N/A",
"recommendation": "If the page contains images, make sure to include descriptive alt text for each image. The alt text should describe the image and include important keywords.",
"example": "<img src='hello-world.jpg' alt= Hello World Image' >"

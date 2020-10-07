var unirest = require("unirest");

var req = unirest("GET", "https://bing-news-search1.p.rapidapi.com/news");

req.query({
	"safeSearch": "Off",
	"textFormat": "Raw"
});

req.headers({
	"x-rapidapi-host": "bing-news-search1.p.rapidapi.com",
	"x-rapidapi-key": "SIGN-UP-FOR-KEY",
	"x-bingapis-sdk": "true",
	"useQueryString": true
});


req.end(function (res) {
	if (res.error) throw new Error(res.error);

	console.log(res.body);
});

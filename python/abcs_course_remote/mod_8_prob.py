'''
Prompt #1
Word Count
Given a long text string, count the number of occurrences of each word. Ignore case. Assume the boundary of a word is whitespace - a " ", or a line break denoted by "\n". Ignore all punctuation, such as . , ~ ? !. Assume hyphens are part of a word - "two-year-old" and "two year old" are one word, and three different words, respectively. 

Return the word counts as a string formatted with line breaks, in no particular order.

Example:
"I do not like green eggs and ham,
I do not like them, Sam-I-Am"

Output:
i 2
do 2
not 2
like 2
green 1
eggs 1
and 1
ham 1
them 1
sam-i-am 1

Also Valid:
and 1
do 2
eggs 1
green 1
ham 1
i 2
like 2
not 2
sam-i-am 1
them 1
'''
example = "I do not like green eggs and ham, I do not like them, Sam-I-Am"


def count_words(text):
  list_of_words = text.split(" ")
  count_map = {}
  for word in list_of_words:
    count_map[word] = count_map.get(word, 0) + 1

  # print in special frequency

  print(count_map)


count_words(example)

'''
Prompt #2
Log Frequency
You are given a stream of logging statements for a server as a list. Your product manager wants to know what categories of error are the most common, as well as what errors in the most common categories are the most common. 

Here are a few log lines, each is a string structured similarly to this:
[
'[WARNING] 403 Forbidden: No token in request parameters',
'[ERROR] 500 Server Error: int is not subscriptable',
'[INFO] 200 Login Successful',
'[INFO] 200 User sent a message',
'[ERROR] 500 Server Error: int is not subscriptable'
]

Return a dictionary with logging statistics, that is formatted like so ( don't worry about spacing or formatting, only the data matters )
 
{
	'WARNING': {
		'403': {
			'Forbidden': {
				'No token in request parameters': 1
			}
		}
	},
	'ERROR': {
		'500': {
			'Server Error': {
				'int is not subscriptable': 2
			}
		}
	},
	'INFO': {
		'200': {
			'OK': {
				'Login Successful': 1,
				'User sent a message': 1
			}
		}
	}
}

When printed it will more likely look like this:
 
{'WARNING': {'403': {'Forbidden': {'No token in request parmeter'}}}}
'''
test_data = [
    '[WARNING] 403 Forbidden: No token in request parameters',
    '[ERROR] 500 Server Error: int is not subscriptable',
    '[INFO] 200 OK: Login Successful',
    '[INFO] 200 OK: User sent a message',
    '[ERROR] 500 Server Error: int is not subscriptable'
]


def log_stats(logs):
  ## get all the data separated
    for log_line in logs:
       ## error_key
       end_bracket = log_line.find(']')
       error_key = log_line[1:end_bracket]
       ## error_number
       error_number = log_line[end_bracket+2:end_bracket+5]
       ## error_name
       end_colon = log_line.find(':')
       error_name = log_line[end_bracket+6:end_colon]
       ## error_message
       error_message = log_line[end_colon+2:]
       print(error_message)
  ## insert all of the data into the right position inside the nested dictionary
    ## create a count map
    count_map = {}
    ## insert sub-maps when there are no exisiting maps
    if not count_map:
      count_map.append(
          {error_key: {error_number: {error_name: {error_message: 1}}}})


print(log_stats(test_data))

# -*- coding: utf-8 -*-
# filename          : main.py
# description       : Changes all tenses to present
# author            : Ian, Travis
# email             : ianault2022@isd282.org, 
# date              : 02-04-2021
# version           : v1.0
# usage             : python main.py
# notes             :
# license           : MIT
# py version        : 3.8.2 (must run on 3.6 or higher)
#==============================================================================
import json


input_text = input("Enter a body of text to be changed into the present tense (press enter to use a sample sentance)\n> ")
input_text = input_text if input_text.strip() else "Since the birth of the software development discipline, programmers have dedicated time and effort into creating digital tools that optimize the process of going from an initial idea to a fully fledged product. This task is a hard one. How do you model a tool to support the non-linear, unstructured process of thinking? How do you create a tool that allows you to turn your thoughts into a digital document? A tool where you can build upon this document, iterate away on tangents when you get inspired, and quickly revert to a former state if this proved unsuccessful? More important, how do you create a tool that allows a group of people to collaborate on the same project, when that project doesn't have a structured form yet?"
punctuations = [".", ",", ":", ";", "!", "?"]
tense_options = {
	"present_1st":        0,  # Present Simple / 1st Person (I / you / we / they)
	"present_3rd":        1,  # Present Simple / 3rd Person (he / she / it)
	"past_simple":        2,  # Past Simple (all)
	"past_participle":    3,  # Past Participle (all)
	"present_participle": 4,  # Present Participle (-ing) (all)
}

tense = tense_options["present_3rd"]


def read_file(filename):
	with open(filename, "r") as file:
		data = file.read()

	return data

def main():
	# list of lists [[present_tense_verb,verb],[present_tense_verb,verb]]
	verbs = json.loads(read_file("verbs.json"))
	formatted_text = []

	for word in input_text.split():
		formatted_word = None
		for verb in verbs:
			for punctuation in punctuations:
				if word.strip(punctuation) in verb:
					if word[-1] == punctuation:
						formatted_word = verb[0] + punctuation
					else:
						formatted_word = verb[0]
					print(f"{word} -> {formatted_word}")
					word = formatted_word
					break
				# optimization
				if formatted_word:
					break
			# optimization
			if formatted_word:
				break
		
		formatted_text.append(word)
	# print(verbs)

	formatted_text = " ".join(formatted_text)
	print(f"\nOutput:\n{formatted_text}")


if __name__ == "__main__":
	main()

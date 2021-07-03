from abc import abstractmethod
import re
 
from sky import getSkyHeadline, getSkyOthers
from bbc import getBbcHeadline, getBbcOthers
from register import getRegister


stories = []

def getStories(onlyNew=False):
    def getAll():
        stories.append(getSkyHeadline())
        for story in getSkyOthers():
            stories.append(story)

        stories.append(getBbcHeadline())   
        for story in getBbcOthers():
            stories.append(story)

        for story in getRegister():
            stories.append(story)

    if onlyNew == False:    # ie: get all stories
       getAll()

    else:   # ie : get only the stories that have come up since last time it was ran
        with open('previousStories.txt') as prevStoriestxt:
            prevStories = prevStoriestxt.read()
            getAll()
            


def printTitles():
    for number, story in enumerate(stories):
        if story.isHeadline:
            print(f"{number + 1}.   HEADLINE:   {story.title}\n")
        elif not story.isHeadline:
            print(f"{number + 1}.    {story.title}\n")

if __name__ == "__main__":
    getStories()
    printTitles()
    def getFollowInput(maxStory):    
        storyToFollowRaw = input("Please enter the number of the story you would like to follow up on!")
        if re.search('[a-zA-Z]', storyToFollowRaw) or int(storyToFollowRaw) < 1 or int(storyToFollowRaw) > maxStory:
            print(f"Please ONLY enter a number between 1 and {maxStory}")
            return int(getFollowInput(maxStory))
        else:
            return int(storyToFollowRaw)

    toFollow = getFollowInput(len(stories))
    print(stories[toFollow - 1].link)


# bug : bbc module adding a story as headline and normal story

# to-do: remove main.py global var stories, change so that getStories() returns the list of stories instead of adding to global var 



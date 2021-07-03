import re
 
from sky import getSkyHeadline, getSkyOthers
from bbc import getBbcHeadline, getBbcOthers
from register import getRegister


stories = []

def getAllStories():
    stories.append(getSkyHeadline())
    for story in getSkyOthers():
        stories.append(story)

    stories.append(getBbcHeadline())   
    for story in getBbcOthers():
        stories.append(story)

    for story in getRegister():
        stories.append(story)

def printTitles():
    for number, story in enumerate(stories):
        if story.isHeadline:
            print(f"{number + 1}.   HEADLINE:   {story.title}\n")
        elif not story.isHeadline:
            print(f"{number + 1}.    {story.title}\n")

if __name__ == "__main__":
    getAllStories()
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

# change

# change 2

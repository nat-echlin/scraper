from abc import abstractmethod
from os import close
import re
 
from sky import getSkyHeadline, getSkyOthers
from bbc import getBbcHeadline, getBbcOthers
from register import getRegister


stories = []

def getAll(arr):
        arr.append(getSkyHeadline())
        for story in getSkyOthers():
            arr.append(story)

        arr.append(getBbcHeadline())   
        for story in getBbcOthers():
            arr.append(story)

        for story in getRegister():
            arr.append(story)

def getStories(onlyNew=False):
    if onlyNew == False:    # ie: get all stories
        getAll(stories)
        
    else:   # ie : get only the stories that have come up since last time it was ran
        with open('previousStories.txt', 'r') as prevStoriestxt:
            prevStoriesRaw = prevStoriestxt.read()
            prevStories = prevStoriesRaw.split('\n')
            allStories = []
            getAll(allStories)
            for story in allStories:
                isValid = True
                for pStory in  prevStories:
                    if pStory == story.title:
                        isValid = False
                        break
                if isValid:
                    stories.append(story)
    
def printTitles():
    for number, story in enumerate(stories):
        if story.isHeadline:
            print(f"{number + 1}.   HEADLINE:   {story.title}\n")
        elif not story.isHeadline:
            print(f"{number + 1}.    {story.title}\n")



if __name__ == "__main__":
    def showStories(onlyNew=False):
        getStories(onlyNew)
        if len(stories) == 0 and onlyNew == True:
            print("\nThere are no new stories! Come back soon! :)         (or I'm broken)\n\n")
        
        else:
            printTitles()
            def getFollowInput(maxStory):    
                storiesToFollowRaw = input("Please enter the numbers of the stories you would like to follow up on! Enter multiples with spaces inbetween, like so: '2 5 12 3'\n")
                # print("\n")
                follows = storiesToFollowRaw.split(" ")
                isValid = True
                for inputted in follows:
                    # work here
                    if re.search('[a-zA-Z]', inputted) or int(inputted) > maxStory:
                        isValid = False
                        break

                if not isValid:
                    print(f"Please ONLY enter NUMBERS (as numerals eg 1 8 19) between 1 and {maxStory}")
                    return getFollowInput(maxStory)        # this reruns the fn, taking user back to input phase

                else:
                    return follows     

                # if re.search('[a-zA-Z]', storyToFollowRaw):
                #     print(f"Please ONLY enter a number between 1 and {maxStory}")
                #     return int(getFollowInput(maxStory))
                # else:
                #     return storyToFollowRaw     # this reruns the fn, taking user back to input phase

            toFollow : list = getFollowInput(maxStory=len(stories))
            for index, story in enumerate(toFollow):
                print(f"{stories[int(story) - 1].title}     {stories[int(story) - 1].link} ")

        # this writes all stories currently on the sites to the previosstories txt

        with open('previousStories.txt', 'w') as prevStoriestxt:
            currentStories = []
            getAll(currentStories)
            for story in currentStories:
                prevStoriestxt.write(f"{story.title}\n")
    
    def getMode():
        mode = input("Select mode: \n1. Only show stories that have been published since last run (and are on the front page currently)\n2. Show all stories currently on the front page\n")
        print("\n")      # all this does is make it look nicer in terminal
        if re.search('[a-zA-Z]', mode):
            print(f"Please ONLY enter '1' or '2'")
            return int(getMode())
        else:
            return int(mode) 

    mode = getMode()   
    # mode = 1        # REMOVE ME     
    if mode == 1:        # new stories
        showStories(onlyNew=True)

    elif mode == 2:        # all stories
        showStories()
    else:
        print("Something's gone seriously wrong.")
        close
    
    


# bug : bbc module adding a story as headline and normal story

# to-do: remove main.py global var stories, change so that getStories() returns the list of stories instead of adding to global var 



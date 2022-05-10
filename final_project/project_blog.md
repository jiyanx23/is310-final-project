# Project Blog Post
## Project Creation

Among all the definition of Digital Humanity provided on the [what's humanity website](https://whatisdigitalhumanities.com/), this one is the closest to what we would've define it ourself. It quotes "The use of information technology and software with humanities source materials to pursue research questions" by Elizabeth McAulay. 

To us, digital humanity utilizes technology to explore human culture. We set our goal to explore the social media platform because it's a place where huge amount of human interaction is happening every minute. Of all the social media platforms, we chose to do Twitch, the streaming platform. Twitch is an interesting example of how the communities are built around individual streamer and also how different culture exist among those groups. We also get some inspiration from the article that we came across. It's an article about how Twitch is used by people to cope with their difficulties in life. "It is clear from our research that streamers, supported by platforms such as Twitch, do serve an important purpose for people that are active on the platform and are going through a difficult time, even without consciously attempting to do so" ((de Wit et al. Live streams on twitch help viewers cope with difficult periods in life)). "Why is Twitch so popular and how is used to build human subculture" is the ultimate question we are trying to answer by this project. We did came up our research questions around this topic. 

For the tools and methodology used in the project, we decided to use python and some sort of visualization to explore the dataset. We did this not only because python is used as the primary programming language in the course, but also is ranked as the top tools used in humanity research (Barbot et al. WHICH DH TOOLS ARE ACTUALLY USED IN RESEARCH?). We decided to use some sort of statistics and techniques for grouping up data to reflect the changes and pattern of our data.
## Data Collection and Cleaning
From the in class reading "Getting know your data", we learned that we needed to ask questions about available datasets (Krause Data Biographies: Getting to know your data). Where did it come from? Who collected it? How was it collected? Most importantly, why was it collected? Those four questions completes the data biography and by knowing our data, we can discover bias.

We can apply the four questions to our first dataset on kaggle. Kaggle is a really popular site for accessing publicly available datasets. Despite its popularity, we can't not evaluate the credibility of the website as individual publisher doesn't need to go through verification process and the datasets can be purely misleading or fabricated information. That's why we will be asking the four questions. The first dataset that we collected was pretty organized. The author of the dataset is a Twitch enthusiast, and he provides clear motivation for collecting and publishing the dataset. However, he doesn't provide any detail about the collection and curation process of the dataset. As we looked through the content of the dataset, we saw that the values in each column were reasonable. They were not just randomly selected, and they seemed right as we could verify using our own knowledge about Twitch. The dataset has 1000 rows, and no empty value. After evaluation, we came to a conclusion that this dataset is credible and can be used in our project.

We don't need to worry about the data biography for our second dataset because it's collected by ourselves, but we do need to worry about what is being collected. After collecting the data, we found out that the Twitch API interface is pretty limited with what data can be collected. It can only collect the top streamer at the time of collection, and is limited to 100 people. The data returned only has couple useful feature that can be used in our project. Since multiple json dataset are being collected for each day, we spent most of the time putting all the small dataset together, updating and reorganizing the final dataset. We found the process extremely tedious and tiring. We weren't equipped with the skills to curate data automatically, so we had to do it manually. We did go through every row and cross examine every datasets, but we could still potentially make mistakes during the process.
## Analysis


## Future


## Reference
de Wit, Jan, et al. “Live Streams on Twitch Help Viewers Cope with Difficult Periods in Life.” Frontiers, Frontiers, 1 Jan. 1AD, https://www.frontiersin.org/articles/10.3389/fpsyg.2020.586975/full. 

Barbot, Laure, et al. WHICH DH TOOLS ARE ACTUALLY USED IN RESEARCH?, 6 Dec. 2019, https://weltliteratur.net/dh-tools-used-in-research/. 

Krause, Heather. “Data Biographies: Getting to Know Your Data.” Global Investigative Journalism Network, 8 Mar. 2021, https://gijn.org/2017/03/27/data-biographies-getting-to-know-your-data/. 
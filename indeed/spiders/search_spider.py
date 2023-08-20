import scrapy
import re
import json
from scrapy_splash import SplashRequest

class IndeedJobSpider(scrapy.Spider):
    name = 'indeed_jobs'
    start_urls = ['https://in.indeed.com/jobs?q=python+developer&l=Kerala&vjk=372ecad0fcaac92a']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 5})

    def parse(self, response):

        # response.css('article.product_pod')
        # Extract job titles
        # breakpoint()
        # breakpoint()
        salary_range = response.xpath('//div[@class="attribute_snippet"]/text()').get()
        print(salary_range,)

        script_tag  = re.findall(r'window.mosaic.providerData\["mosaic-provider-jobcards"\]=(\{.+?\});', response.text)
        if script_tag is not None:
            json_blob = json.loads(script_tag[0])
        
        jobs_list = json_blob['metaData']['mosaicProviderJobCardsModel']['results']
        # print(jobs_list,end=" ")
        
        for job in jobs_list:
            print(job)
            breakpoint()
            job_name = job.get('displayTitle', 'N/A')
            job_location = job.get('formattedLocation', 'N/A')
            
            # Extract the salary text from the 'salarySnippet' dictionary
            max = job.get('estimatedSalary','N/A')
            min=job.get('estimatedSalary')
            
            
            
            
            print(f"Job Name: {job_name}")
            print(f"Job Location: {job_location}")
            # print(f"Salary Info: {salary_snippet}")
            print(max,min)
            print("-" * 40)

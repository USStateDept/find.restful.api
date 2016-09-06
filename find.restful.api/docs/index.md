# Welcome to find.restful.api

To see our repository on GitHub visit [here](https://github.com/USStateDept/find.restful.api).

## API Endpoints

    categories/     # You can query based on 'category' (category name) and/or 'subcategory' (subcategory name)
        list/       # You can request all categories
    
    countries/      # You can query based on 'country' (country name)
        list/       # You can request all countries
    
    countries/data/ # You can query based on 'country' (country id) and 'indicator' (indicator id) with 'year'
                    # Note: without specifying year it will default to 'all'
    
    indicators/     # You can query based on 'indicator' (indicator name)
        list/       # You can request all indicators
    
    regions/        # You can query based on 'region' (region id)
        list/       # You can request all regions
    
    region/data/    # You can query based on 'region' (region id) and 'indicator' (indicator id) with 'year'
                    # Note: without specifying year it will default to 'all'
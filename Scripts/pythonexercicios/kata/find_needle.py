def find_needle(haystack):
    if 'needle' in haystack:
        return f'found the needle at position {haystack.index("needle")}'
    else:
        return 'neelde not found!'
        
haystack = ["hay", "junk", "hay","needle", "hay", "moreJunk", "randomJunk"]
print(find_needle(haystack))

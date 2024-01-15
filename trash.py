l = {
            "ops": [
                {
                    "insert": "Data science is an interdisciplinary academic field that uses statistics, scientific computing, scientific methods, processes, algorithms and systems to extract or extrapolate knowledge and insights from potentially noisy, structured, or unstructured data.",
                    "attributes": {
                        "color": "#bdc1c6"
                    }
                },
                {
                    "insert": "\n\n"
                },
                {
                    "insert": "dadada bilalda dadad AAAAAAAAAAAAAAAAAAAAA.",
                    "attributes": {
                        "background": "#202124",
                        "color": "#bdc1c6"
                    }
                },
                {
                    "insert": "\n"
                }
            ]
        }

b = ''
for a in range(0,len(l['ops'])):
    print(l['ops'][a]['insert'])
    b += l['ops'][a]['insert']
print(b.replace('\n',' '))
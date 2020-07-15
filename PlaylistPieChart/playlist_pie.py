import httpx
import matplotlib.pyplot as plt


usercount = {}
offset = 0
headers = {'Authorization': 'Bearer BQCMggyUpJL4HF891ggF7P4X4MU6suXyua1AmNTz3meu3Mp7uSmMZJ8cON0fS9za2SlpvrIvp75wVfD9R4o4nTwOPDRslW2LZbyIygQek-RmTJtKR6oGtb21dH9lBc0ZjpEjs18BNzt6AN4'}
total = 0

while True:
    
    r = httpx.get(f"https://api.spotify.com/v1/playlists/3TT7tx7TJCgFRkGnDL5BnK/tracks?fields=total%2Climit%2Citems(added_by.id)&offset={offset}", headers=headers)
    json = r.json()
    
    for user in json['items']:
        user_id = user['added_by']['id']
        if user_id in usercount.keys():
            usercount[user_id] += 1
        else:
            usercount[user_id] = 1

    total += len(json['items'])

    if len(json['items']) < 100:
        break
    else:
        offset += 100

usercount['Kozicki'] = usercount['mljn1v36gzolcxc0y8ftgktgg']
del usercount['mljn1v36gzolcxc0y8ftgktgg']

usercount['Matt'] = usercount['11165717538']
del usercount['11165717538']

usercount['Joe'] = usercount['7vfkhiw25evlxmbbovz897izb']
del usercount['7vfkhiw25evlxmbbovz897izb']

usercount['benisjoke'] -= 12
usercount['finch'] = 12

print(usercount)
print(total)


# Data to plot
labels = usercount.keys()
sizes = usercount.values()

# Plot
plt.pie(sizes, labels=labels,
autopct='%1.1f%%')

plt.axis('equal')
plt.show()
def pythogorean_triplets(a):
    for i in range(1,a):
        for j in range(i,a):
            for k in range(j,a):
                if i**2+j**2==k**2 and i+j+k==1000:
                    print(f"{i}^2+{j}^2={k}^2")
                    break
pythogorean_triplets(1000)
#200,375,425
#31875000
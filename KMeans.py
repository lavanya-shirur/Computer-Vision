class KmeansSegmentation:

    def segmentation_grey(self, image, k = 2):
        """Performs segmentation of an grey level input image using KMeans algorithm, using the intensity of the pixels as features
        takes as input:
        image: a grey scale image
        return an segemented image
        -----------------------------------------------------
        Sample implementation for K-means
        1. Initialize cluster centers
        2. Assign pixels to cluster based on (intensity) proximity to cluster centers
        3. While new cluster centers have moved:
            1. compute new cluster centers based on the pixels
            2. Assign pixels to cluster based on the proximity to new cluster centers

        """

        return image


    def segmentation_rgb(self, image, k=2):
        """Performs segmentation of a color input image using KMeans algorithm, using the intensity of the pixels (R, G, B)
        as features
        takes as input:
        image: a color image
        return an segemented image"""

        
         iterations = 5
       
        print(image.shape)
        imageW = image.shape[0]
        imageH = image.shape[1]


        dataVector = np.ndarray(shape=(imageW * imageH, 5), dtype=float)
       
        pixelClusterAppartenance = np.ndarray(shape=(imageW * imageH), dtype=int)

       
        for y in range(0, imageH):
            for x in range(0, imageW):
                xy = (x, y)
              
                rgb=image[x,y]
                print(rgb)
                #rgb = image.getpixel(xy)

                dataVector[x + y * imageW, 0] = rgb[0]
                dataVector[x + y * imageW, 1] = rgb[1]
                dataVector[x + y * imageW, 2] = rgb[2]
                dataVector[x + y * imageW, 3] = x
                dataVector[x + y * imageW, 4] = y
        print("data vector")
        print(dataVector)
      
        dataVector_scaled = preprocessing.normalize(dataVector)
        minValue = np.amin(dataVector_scaled)
        maxValue = np.amax(dataVector_scaled)

        centers = np.ndarray(shape=(k,5))
        for index, center in enumerate(centers):
            centers[index] = np.random.uniform(minValue, maxValue, 5)
        print("center")
        print(centers[index])

        for iteration in range(iterations):
           
            for idx, data in enumerate(dataVector_scaled):
                distanceToCenters = np.ndarray(shape=(k))
                for index, center in enumerate(centers):
                    distanceToCenters[index] = euclidean_distances(data.reshape(1, -1), center.reshape(1, -1))
                pixelClusterAppartenance[idx] = np.argmin(distanceToCenters)

           
            clusterToCheck = np.arange(k)  
           
            clustersEmpty = np.in1d(clusterToCheck, pixelClusterAppartenance)
           
            for index, item in enumerate(clustersEmpty):
                if item == False:
                    pixelClusterAppartenance[np.random.randint(len(pixelClusterAppartenance))] = index
                

        for i in range(k):
            dataInCenter = []

            for index, item in enumerate(pixelClusterAppartenance):
                if item == i:
                    dataInCenter.append(dataVector_scaled[index])
            dataInCenter = np.array(dataInCenter)
            centers[i] = np.mean(dataInCenter, axis=0)

       
        print("Centers Iteration num", iteration, ": \n", centers)

       
        for index, item in enumerate(pixelClusterAppartenance):
            dataVector[index][0] = int(round(centers[item][0] * 255))
            dataVector[index][1] = int(round(centers[item][1] * 255))
            dataVector[index][2] = int(round(centers[item][2] * 255))

       
        image = Image.new("RGB", (imageW, imageH))

        for y in range(imageH):
            for x in range(imageW):
                image.putpixel((x, y), (int(dataVector[y * imageW + x][0]),
                                        int(dataVector[y * imageW + x][1]),
                                        int(dataVector[y * imageW + x][2])))

        print(type(image))
        image = cv2.cvtColor(np.asarray(image), cv2.COLOR_BGR2GRAY)
        print(type(image))
        
        return image

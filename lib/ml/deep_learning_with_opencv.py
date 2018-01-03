import numpy as np,argparse,time,cv2
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help="path to input image")
ap.add_argument('-p','--prototxt',required=True,help='path to Caffe ')
ap.add_argument('-m','--model',requird=True,help='qweqwe')
ap.add_argument('-l','--labels',requird=True,help='werer')
args = vars(ap.parse_args())
image = cv2.imread(args['image'])
rows = open(args['labels']).read().strip().split('\n')
classes = [r[r.find("")+1:].split(',')[0] for r in rows]
blob = cv2.dnn.blobFromImage(image,1,(224,224),(104,117,123))
print("INFO load model")
net = cv2.dnn.readNetFromCaffe(args['prototxt'],args['model'])
net.setInput(blob)
start = time.time()
preds =net.forward()
end  =time.time()
print("INFO classes took{:.5} seconds".format(end -start))
idxs = np.argsort(preds[0])[::-1][:5]
for(i,idx) in enumerate(idxs):
    if i==0:
        text = "Label:{},{:.2f}%".format(classes[idx]),preds[0][idx]*100
        print("INFO {} . label :{}, provavility:{:.5}".format(i+1,classes[idx],preds[0][idx]))
    cv2.imshow("image",image)
    cv2.waitKey(0)
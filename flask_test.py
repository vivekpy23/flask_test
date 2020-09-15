import time, ast

from flask import Flask, jsonify, request
app = Flask(__name__)





@app.route('/ping', methods= ['GET'])
def view_health():
	try:
		return jsonify({'status':200,'msg':'Health check succeeded.'})
	except Exception as ex:
		return jsonify({'status':500,'msg':'Failure Health check.'})


@app.route('/execution-parameters', methods = ['GET'])
def params():
	



def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[high]
 
    for j in range(low, high):
 
        if arr[j] <= pivot:
 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):

    if len(arr) == 1:
        return arr
    if low < high:
 
        pi = partition(arr, low, high)
 
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


@app.route('/sort', methods= ['POST'])
def sorting():
	concurrent = request.args.get("concurrent")
	input_list = ast.literal_eval(request.args.get("input_list"))

	start_time = time.time()
	quickSort(input_list, 0, len(input_list) - 1)
	duration = 	time.time() - start_time

	return jsonify({'time-taken': duration, 'sorted-list': input_list})


#curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/sort -d '{"concurrent":"True", "input_list":[5,3,0,2]}'


if __name__ == '__main__':
	app.run()
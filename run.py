import uvicorn

if __name__ == '__main__':
    uvicorn.run('wechat_robot:app', host='0.0.0.0', port=80, reload=True, debug=True)
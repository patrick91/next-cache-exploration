# Next.js cache exploration

To run, start the backend first, you can do so by using docker:

```
cd backend
docker build -t next-backend-for-cache .
docker run -p 8000:8000 next-backend-for-cache
```

Then in another terminal:

```
cd frontend
pnpm i
pnpm run build
pnpm start
```

Now you can go to http://localhost:3000 and see the requests done
to the backend service in it's terminal
export default async function Home() {
  const query = `
    query {
      country(code: "CH") {
        name
      }
    }`;

  const qs = new URLSearchParams({ query });
  // const url = `http://localhost:8000?${qs.toString()}`;
  const url = `http://localhost:8000`;

  const data = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ query }),
    next: {
      revalidate: 5,
    },
  }).then((res) => res.json());

  return (
    <pre>
      <code>{JSON.stringify(data, null, 2)}</code>
    </pre>
  );
}

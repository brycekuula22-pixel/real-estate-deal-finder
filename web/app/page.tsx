export default function HomePage() {
  return (
    <main style={{padding: "40px", fontFamily: "Arial"}}>

      <h1>Find the best multifamily deals in Minneapolis in seconds</h1>

      <p>
        Analyze duplexes, triplexes, and fourplexes with real investment metrics.
      </p>

      <br/>

      <a href="/search">
        <button style={{
          padding: "12px 24px",
          fontSize: "16px",
          cursor: "pointer"
        }}>
          Start Searching Deals
        </button>
      </a>

      <br/><br/>

      <h2>Example Deals</h2>

      <p>• NE Minneapolis Duplex — 8.4% Cap Rate</p>
      <p>• St Paul Triplex — $620/month Cash Flow</p>
      <p>• Uptown Fourplex — 14.2% Cash-on-Cash Return</p>

    </main>
  )
}
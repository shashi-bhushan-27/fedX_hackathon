import { useState, useEffect } from "react"
import { ingestCase, predict, allocate, metrics, copilot } from "../api"

export default function FedexDashboard() {

  const [form, setForm] = useState({
    amount: "", due_days: "", invoice_count: "", credit_score: "",
    previous_collections: "", historical_default_rate: "",
    debt_to_credit_ratio: "", invoice_intensity: "",
    region: "", specialization: ""
  })

  const [result, setResult] = useState(null)
  const [kpis, setKpis] = useState({})
  const [question, setQuestion] = useState("")
  const [answer, setAnswer] = useState("")

  useEffect(() => { metrics().then(setKpis) }, [])

  const runAI = async () => {
    const payload = {...form}
    Object.keys(payload).forEach(k => {
      if (!isNaN(payload[k])) payload[k] = Number(payload[k])
    })

    await ingestCase(payload)
    const pred = await predict(payload)
    const alloc = await allocate({ ...payload, ...pred })

    setResult({ ...pred, ...alloc })
    metrics().then(setKpis)
  }

  return (
    <div style={{ padding: 20 }}>
      <h1>FLEX-DCA FedEx Control Center</h1>

      <h3>New Case</h3>
      {Object.keys(form).map(k =>
        <input key={k} placeholder={k}
          onChange={e => setForm({ ...form, [k]: e.target.value })} />
      )}
      <br/>
      <button onClick={runAI}>Run AI</button>

      {result && <>
        <h3>AI Output</h3>
        <pre>{JSON.stringify(result, null, 2)}</pre>
      </>}

      <h3>Live KPIs</h3>
      <pre>{JSON.stringify(kpis, null, 2)}</pre>

      <h3>Compliance Copilot</h3>
      <input placeholder="Ask SOP..."
             onChange={e => setQuestion(e.target.value)} />
      <button onClick={() => copilot(question).then(r => setAnswer(r.answer))}>
        Ask
      </button>
      <pre>{answer}</pre>
    </div>
  )
}

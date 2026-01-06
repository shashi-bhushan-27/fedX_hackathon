export default ({data}) => (
<table>
<tr><th>Case</th><th>Amount</th><th>Status</th></tr>
{data.map(c=>(
<tr key={c.case_id}>
<td>{c.case_id}</td>
<td>{c.amount}</td>
<td>{c.status}</td>
</tr>
))}
</table>
);

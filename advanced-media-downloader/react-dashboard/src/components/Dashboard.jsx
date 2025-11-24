import React, {useEffect, useState} from 'react'
import io from 'socket.io-client'

export default function Dashboard(){
  const [tasks, setTasks] = useState([])
  useEffect(()=>{
    const s = io(import.meta.env.VITE_BACKEND || 'http://localhost:8000')
    s.on('connect', ()=> console.log('ws connected'))
    s.on('task-update', data => setTasks(prev => [data, ...prev].slice(0,20)))
    return ()=> s.disconnect()
  }, [])

  return (
    <div>
      <h2>Recent Task Updates</h2>
      <ul>
        {tasks.map(t => (<li key={t.id}>{t.id} — {t.status} — {t.source_url}</li>))}
      </ul>
    </div>
  )
}

import Alert from 'react-bootstrap/Alert'

function LowPrice () {

    return (
        <>
            <Alert
              variant='info'
              style={{
                position: 'fixed',
                top: 10,
                right: 10,
                zIndex: 9999,
                width: '300px',
                height: '150px'
              }}>
                It worked!
            </Alert>
        
        </>
    )
}

export default LowPrice
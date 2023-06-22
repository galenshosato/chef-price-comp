import PriceCard from "./PriceCard"

function PriceDisplay({items}) {
    return (
        <div style={{width: '1900px', flexWrap: 'wrap'}} className="d-flex justify-content-center">
            {items.map((item) => {
                return <PriceCard key={item.id} item={item} />
            })}
        </div>
    )
}

export default PriceDisplay
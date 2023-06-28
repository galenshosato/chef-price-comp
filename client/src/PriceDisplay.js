import PriceCard from "./PriceCard"

function PriceDisplay({items, noProduct}) {
    return (
        <>
        { noProduct ? 
        <h2 className="d-flex justify-content-center">
            Item not found. Please re-enter desired product.
        </h2> :
        <div style={{width: '1900px', flexWrap: 'wrap'}} className="d-flex justify-content-center">
            {items.map((item) => {
                return <PriceCard key={item.id} item={item} />
            })}
        </div>}
        </>
    )
}

export default PriceDisplay
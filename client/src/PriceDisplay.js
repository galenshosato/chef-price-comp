import PriceCard from "./PriceCard"

function PriceDisplay({items}) {
    return (
        <>
            {items.map((item) => {
                return <PriceCard key={item.id} item={item} />
            })}
        </>
    )
}

export default PriceDisplay
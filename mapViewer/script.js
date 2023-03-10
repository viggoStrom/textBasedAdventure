
// importing map

fetch("map.json").then((response) => response.json()).then((json) => {
    main(json)
})

// \importing map

function main(json) {

    // setting grid size

    const mapGrid = document.getElementById("mapGrid")

    const gridRows = json.meta.rows
    const gridColumns = json.meta.columns

    mapGrid.style.aspectRatio = gridColumns / gridRows
    mapGrid.style.gridTemplateColumns = ""
    mapGrid.style.gridTemplateRows = ""

    let newWidth = ""
    let newHeight = ""

    for (let index = 0; index < gridColumns; index++) {
        newWidth = newWidth.concat("auto ")
    }
    for (let index = 0; index < gridRows; index++) {
        newHeight = newHeight.concat("auto ")
    }

    mapGrid.style.gridTemplateColumns = newWidth
    mapGrid.style.gridTemplateRows = newHeight

    // \setting grid size


    // populating grid

    const coordinates = document.querySelector("aside p:first-of-type")
    const detailsPanel = document.querySelector("#detailsPanel")

    let colors = ["lightGray", "white"]
    let colorBit = 1

    for (let y = 0; y < gridRows; y++) {
        for (let x = 0; x < gridColumns; x++) {

            const newDiv = document.createElement("div")
            newDiv.className = "mapSquare"
            newDiv.id = `x` + x
            newDiv.id += `y` + y
            newDiv.onclick = showDetails = (event) => {
                // shows details of square

                coordinates.innerHTML = event.srcElement.id

                detailsPanel.children.forEach((element) => {
                    element.remove()
                })
                const currentSquare = json.rooms[event.srcElement.id]

                for (const [key, value] of Object.entries(currentSquare)) {
                    const keySpan = document.createElement("span")
                    const valueSpan = document.createElement("span")

                    keySpan.innerHTML = key + ": "
                    if (typeof (value) == Object) {
                        console.log(Object.keys(value));
                        Object.keys(value).forEach(element => {
                            console.log(element);
                            valueSpan.innerHTML += value[element] + ", "
                        })
                        keySpan.appendChild(valueSpan)
                    } else {
                        keySpan.appendChild(valueSpan)
                        valueSpan.innerHTML = value
                    }

                    detailsPanel.appendChild(keySpan)
                }

                // \shows details of square
            }
            newDiv.style.backgroundColor = colors[colorBit]
            if (colorBit == 0) {
                colorBit = 1
            } else {
                colorBit = 0
            }
            mapGrid.appendChild(newDiv)
        }
    }

    // \populating grid


    // make square borders reflect allowed directions

    Object.keys(json.rooms).forEach(room => {
        const thickBorder = "4px solid black"
        directions = json.rooms[room].allowedDirections
        if (directions.north == false) {
            document.getElementById(room).style.borderTop = thickBorder
        }
        if (directions.south == false) {
            document.getElementById(room).style.borderBottom = thickBorder
        }
        if (directions.west == false) {
            document.getElementById(room).style.borderLeft = thickBorder
        }
        if (directions.east == false) {
            document.getElementById(room).style.borderRight = thickBorder
        }
    })

    // \make square borders reflect allowed directions

    // populate details panel


    const template = json.meta.template

    for (const [key, value] of Object.entries(template)) {
        const keySpan = document.createElement("span")
        const valueSpan = document.createElement("span")

        keySpan.innerHTML = key + ": "
        if (typeof (value) == Object) {
            console.log(Object.keys(value));
            Object.keys(value).forEach(element => {
                console.log(element);
                valueSpan.innerHTML += value[element] + ", "
            })
            keySpan.appendChild(valueSpan)
        } else {
            keySpan.appendChild(valueSpan)
            valueSpan.innerHTML = value
        }

        detailsPanel.appendChild(keySpan)
    }

    // \populate details panel
}

import React, { Component } from 'react'
import './DataCircles.css'

export default class DataCircles extends Component {
  constructor() {
    super()
    this.state = {
      onHover: false,
      hoverTicker: null
    }
    this.renderCircles.bind(this)
  }

  onItemMouseOver = (posX, posY, ticker, e) => {
    this.setState({
      onHover: true,
      hoverTicker: ticker,
      hoverX: posX,
      hoverY: posY-7
    })
  }

  onItemMouseOut = (e) => {
    this.setState({onHover: false})
  }

  renderCircles = (props) => {
    const {onHover, hoverTicker, hoverX, hoverY} = this.state
    return (coords, index) => {
      const posX = props.scales.xScale(coords[props.xAccessor])
      const posY = props.scales.yScale(coords[props.yAccessor])
      const ticker = coords['ticker']
      let fill = "rgb(188, 189, 34)"
      if (coords[props.outlierAccessorPos] === 1) {
        fill = "rgb(23, 190, 207)"
      } else if (coords[props.outlierAccessorNeg] === 1) {
        fill = "rgb(214, 39, 40)"
      }
      const circleProps = {
        cx: posX,
        cy: posY,
        r: 4,
        key: index,
        stroke: "blue",
        fill: fill
      };
      return <g key={`group-${index}`}
          onMouseOver={this.onItemMouseOver.bind(this, posX, posY, ticker)}
          onMouseOut={this.onItemMouseOut.bind(this)}>
        <circle {...circleProps}/>
        {onHover && <text
          x={hoverX}
          y={hoverY}
          key={`text-${index}`}>{hoverTicker}</text>}
      </g>
    }
  }

  render() {
    return <g>{ this.props.data.map(this.renderCircles(this.props)) }</g>
  }
}
function removeTags(htmlText) {
    let pureText = ''
    if((htmlText===null)||(htmlText==='')) {
        return false
    } else {
        pureText = htmlText.replace(/(<([^>]+)>)/g, '')
        return pureText
    }
}

export default removeTags()
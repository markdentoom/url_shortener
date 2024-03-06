import React, { Component } from "react"
import PropTypes from "prop-types"
import { connect } from "react-redux"
import { withRouter } from "react-router-dom"
import { deleteNote, updateNote } from "./NotesActions"
import { Button } from "react-bootstrap"

class Note extends Component {
  onDeleteClick = () => {
    const { note } = this.props
    this.props.deleteNote(note.id)
  }
  onUpperCaseClick = () => {
    const { note } = this.props
    this.props.updateNote(note.id, {
      content: note.content.toUpperCase(),
    })
  }
  onLowerCaseClick = () => {
    const { note } = this.props
    this.props.updateNote(note.id, {
      content: note.content.toLowerCase(),
    })
  }
  render() {
    const { note } = this.props
    return (
      <div>
        <hr />
        id: {note.id} - long url: <a href={note.content}>{note.content}</a>
        <br />
        short url: <a href={note.short_url}>{note.short_url}</a>
        <br />
        <Button variant="danger" size="sm" onClick={this.onDeleteClick}>
          Delete
        </Button>
      </div>
    )
  }
}

Note.propTypes = {
  note: PropTypes.object.isRequired,
}
const mapStateToProps = (state) => ({})

export default connect(mapStateToProps, { deleteNote, updateNote })(
  withRouter(Note)
)

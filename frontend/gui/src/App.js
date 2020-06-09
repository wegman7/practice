import React, { Component } from 'react';
import './App.css';
import axios from 'axios';

class App extends Component {

  state = {}

  componentDidMount() {
    axios.get('/api/profile/')
        .then(response => {
            this.setState({
                'profiles': response.data
            });
        })
        .catch(error => {
            console.log(error);
        })
  }

  render() {

    const renderProfiles = () => {
      if (this.state.profiles !== undefined){
        return (
          this.state.profiles.map(profile => <div>{profile.first_name}, {profile.last_name}</div>)
        )
      }
    }

    return (
      <div className="App">
        {renderProfiles()}
      </div>
    );
  }
}

export default App;

import logo from './logo.svg';
import './App.css';
import { Piano, KeyboardShortcuts, MidiNumbers } from 'react-piano';
import 'react-piano/dist/styles.css';


function App() {
    const firstNote = MidiNumbers.fromNote('a2');
  const lastNote = MidiNumbers.fromNote('f5');
  const keyboardShortcuts = KeyboardShortcuts.create({
    firstNote: firstNote,
    lastNote: lastNote,
    keyboardConfig: KeyboardShortcuts.HOME_ROW,
  });

  return (
    <Piano
      noteRange={{ first: firstNote, last: lastNote }}
      playNote={(midiNumber) => {
        console.log(midiNumber);
        const freq = 880 * (2**((midiNumber - 69)/12));
         fetch('http://dubdub.mit.edu:5000/startfreq/' + freq);
      }}
      stopNote={(midiNumber) => {
        const freq = 880 * (2**((midiNumber - 69)/12));
         fetch('http://dubdub.mit.edu:5000/stopfreq/' + freq);
      }}
      width={1000}
      keyboardShortcuts={keyboardShortcuts}
    />
  );
}

export default App;

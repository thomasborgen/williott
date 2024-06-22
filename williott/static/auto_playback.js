/*
To use, add an audio element and give it an ID starting with "audio_" followed by
Whatever will trigger this events id.

id:
<button id="english_name">Name</button>
<audio id="audio_english_name" />

This code will then attach an on click event to the button
that will play the audio whenever it is clicked.
*/
function auto_assign_audio_playback_to_buttons(){
const audio_elements = document.getElementsByTagName("audio");

for (const audio_element of audio_elements) {
  const target_id = audio_element.id.replace("audio_", "");
  const target = document.getElementById(target_id);

  if (target !== null) {

    console.log("added for some reason")
    target.addEventListener("click", () => {
      audio_element.play();
    });
  }
}
}

auto_assign_audio_playback_to_buttons()

document.addEventListener('htmx:afterSettle', function(evt) {
  auto_assign_audio_playback_to_buttons()
});

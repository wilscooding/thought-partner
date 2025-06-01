import { writable } from 'svelte/store';

export const userSelection = writable({
  industry: '',
  capability_area: '',
  personality_type: '',
  gender: '',
  user_input_text: "connect me with a Thought Partner.",

  is_first_message: true
});

export const matchedTP = writable({});

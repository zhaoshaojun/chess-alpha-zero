class PlayDataConfig:
    def __init__(self):
        self.nb_game_in_file = 10
        self.sl_nb_game_in_file = 10
        self.max_file_num = 10


class PlayConfig:
    def __init__(self):
        self.max_processes = 3
        self.search_threads = 16
        self.vram_frac = 0.4
        self.simulation_num_per_move = 10
        self.c_puct = 3
        self.noise_eps = 0.25
        self.dirichlet_alpha = 0.3
        self.change_tau_turn = 40
        self.automatic_draw_turn = 40
        self.virtual_loss = 3
        self.parallel_search_num = 4
        self.prediction_worker_sleep_sec = 0.00001
        self.wait_for_expanding_sleep_sec = 0.000001
        self.resign_threshold = None
        self.min_resign_turn = 5
        self.random_endgame = -1
        self.tablebase_access = False


class EvaluateConfig:
    def __init__(self):
        self.game_num = 10
        self.replace_rate = 0.55
        self.play_config = PlayConfig()
        self.play_config.simulation_num_per_move = 10
        self.play_config.noise_eps = 0
        self.random_endgame = -1
        self.play_config.tablebase_access = False


class PlayWithHumanConfig:
    def __init__(self):
        self.play_config = PlayConfig()
        self.play_config.tablebase_access = False


class TrainerConfig:
    def __init__(self):
        self.batch_size = 32 # 2048
        self.cleaning_processes = 8  # RAM explosion...
        self.vram_frac = 0.2
        self.epoch_to_checkpoint = 1
        self.start_total_steps = 0
        self.save_model_steps = 1000
        self.load_data_steps = 1000
        self.min_data_size_to_learn = 1000
        self.max_num_files_in_memory = 10


class ModelConfig:
    def __init__(self):  # not sure why all the below variables were static. changed.
        self.cnn_filter_num = 16
        self.cnn_filter_size = 3
        self.res_layer_num = 1
        self.l2_reg = 1e-4
        self.value_fc_size = 16
        self.t_history = 1
        self.input_stack_height = 7 + self.t_history*14

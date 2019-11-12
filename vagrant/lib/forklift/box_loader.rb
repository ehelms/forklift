# frozen_string_literal: true

module Forklift
  class BoxLoader

    attr_accessor :locations

    def initialize(root_dir = nil, locations = nil)
      @root_dir = root_dir || default_root_dir
      @locations = locations || default_locations
      @box_factory = BoxFactory.new(versions)
    end

    def load!
      @locations.sort_by { |f| File.basename(f) }.each do |box_file|
        @box_factory.add_boxes!(box_file)
      end
    end

    def boxes
      @box_factory.boxes
    end

    private

    def default_root_dir
      File.join(__dir__, '..', '..')
    end

    def default_locations
      Dir.glob(["#{@root_dir}/boxes.d/*.yaml", "#{@root_dir}/plugins/*/base_boxes.yaml"])
    end

    def versions
      YAML.load_file("#{@root_dir}/config/versions.yaml")
    end

    def box_config
      config = if File.exist?("#{@root_dir}/config/boxes.yaml")
                 "#{@root_dir}/config/boxes.yaml"
               else
                 "#{@root_dir}/config/boxes.all.yaml"
               end

      YAML.load_file(config)
    end

  end
end
